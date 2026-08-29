#!/usr/bin/env python3
"""Test fungsi pure kb.py (stdlib only). Jalankan: python3 scripts/test_kb.py"""
import collections

import kb


def test_accuracy():
    assert kb.accuracy(0, 0) == 0
    assert kb.accuracy(1, 2) == 50
    assert kb.accuracy(5, 7) == 71       # 71.43
    assert kb.accuracy(7, 9) == 78       # 77.78
    assert kb.accuracy(2, 3) == 67       # 66.67
    assert kb.accuracy(12, 16) == 75
    assert kb.accuracy(35, 43) == 81     # 81.40
    assert kb.accuracy(15, 16) == 94     # 93.75
    assert kb.accuracy(1, 8) == 13       # 12.5 → half-up 13
    assert kb.accuracy(3, 8) == 38       # 37.5 → half-up 38


def test_status():
    # Total < 3 → ⚪
    assert kb.status(0, 1) == kb.GREY
    assert kb.status(2, 2) == kb.GREY
    # Ambang
    assert kb.status(4, 7) == kb.RED     # 57%
    assert kb.status(6, 10) == kb.YELLOW  # 60% (batas bawah 🟡)
    assert kb.status(79, 100) == kb.YELLOW  # 79%
    assert kb.status(8, 10) == kb.GREEN  # 80% (batas 🟢)
    assert kb.status(2, 3) == kb.YELLOW  # 67%
    assert kb.status(12, 16) == kb.YELLOW  # 75%
    assert kb.status(22, 25) == kb.GREEN  # 88%


def test_aggregate_quiz():
    baseline = {
        "quiz": {
            "pola": {"L19-なります": {"benar": 22, "total": 25}},
            "partikel": {"に": {"benar": 35, "total": 43}},
            "lesson": {"Lesson 16": {"benar": 12, "total": 16}},
        },
        "jlpt": {},
    }
    attempts = [
        {"kind": "quiz", "questions": [
            {"correct": True, "tags": {"pola": ["L19-なります"], "partikel": ["に"],
                                       "lesson": ["Lesson 19"]}},
            {"correct": False, "tags": {"lesson": ["Lesson 16"]}},
        ]},
        # sesi jlpt TIDAK boleh mempengaruhi agregat quiz
        {"kind": "jlpt", "questions": [
            {"correct": True, "subtype": "MG-yomi"},
        ]},
    ]
    agg = kb.aggregate(baseline, attempts, "quiz")
    assert agg["pola"]["L19-なります"] == {"benar": 23, "total": 26}
    assert agg["partikel"]["に"] == {"benar": 36, "total": 44}
    assert agg["lesson"]["Lesson 16"] == {"benar": 12, "total": 17}  # +1 salah
    assert agg["lesson"]["Lesson 19"] == {"benar": 1, "total": 1}
    # baseline tak termutasi
    assert baseline["quiz"]["pola"]["L19-なります"] == {"benar": 22, "total": 25}


def test_aggregate_jlpt():
    baseline = {"quiz": {}, "jlpt": {"subtype": {"DK-narabekae": {"benar": 7, "total": 9}}}}
    attempts = [
        {"kind": "jlpt", "questions": [
            {"correct": False, "subtype": "DK-narabekae"},
            {"correct": True, "subtype": "MG-yomi"},
        ]},
        {"kind": "quiz", "questions": [{"correct": True, "tags": {"pola": ["X"]}}]},
    ]
    agg = kb.aggregate(baseline, attempts, "jlpt")
    assert agg["subtype"]["DK-narabekae"] == {"benar": 7, "total": 10}
    assert agg["subtype"]["MG-yomi"] == {"benar": 1, "total": 1}
    assert "pola" not in agg  # quiz tak bocor


def test_rank_weak():
    agg = {
        "pola": {
            "A-red": {"benar": 3, "total": 6},    # 50% 🔴
            "B-yel": {"benar": 6, "total": 10},   # 60% 🟡
            "C-green": {"benar": 9, "total": 10},  # 90% 🟢 (tak masuk)
            "D-grey": {"benar": 1, "total": 2},   # ⚪ (tak masuk)
        },
        "lesson": {"E-yel": {"benar": 5, "total": 7}},  # 71% 🟡
    }
    weak = kb.rank_weak(agg)
    tags = [w["tag"] for w in weak]
    assert tags == ["A-red", "B-yel", "E-yel"]  # 🔴 dulu, lalu 🟡 acc asc (60<71)
    assert all(w["status"] in (kb.RED, kb.YELLOW) for w in weak)


def test_spread_positions():
    pos = kb.spread_positions(12, 4, seed=1)
    assert len(pos) == 12
    assert all(1 <= p <= 4 for p in pos)
    counts = collections.Counter(pos)
    assert max(counts.values()) - min(counts.values()) <= 1  # merata
    assert len(set(kb.spread_positions(5, 4, seed=2))) > 1   # tak semua sama


def test_tag_to_lesson():
    assert kb.tag_to_lesson("L16-に-naik") == "Lesson 16"
    assert kb.tag_to_lesson("L4-jam") == "Lesson 4"
    assert kb.tag_to_lesson("bukan-tag") is None


def test_compute_scope_review():
    agg = {
        "pola": {
            "L16-に-naik": {"benar": 3, "total": 5},         # 60% 🟡
            "L15-に-vs-で-statis": {"benar": 5, "total": 7},  # 71% 🟡
            "L19-なります": {"benar": 22, "total": 25},        # 88% 🟢
        },
        "lesson": {"Lesson 16": {"benar": 12, "total": 16}},  # 75% 🟡
    }
    scope = kb.compute_scope(agg, "review", n=12)
    tags = [w["tag"] for w in scope["weights"]]
    assert "L16-に-naik" in tags and "L15-に-vs-で-statis" in tags
    assert "L19-なります" not in tags          # 🟢 tak masuk weak
    assert "Lesson 16" in scope["lessons"]
    assert all(w["n"] > 0 for w in scope["weights"])


def test_session_deltas():
    baseline = {"quiz": {"pola": {"X": {"benar": 5, "total": 7}}}, "jlpt": {}}
    session = {"kind": "quiz", "questions": [
        {"correct": True, "tags": {"pola": ["X"]}},    # X: 5/7 → 6/8
        {"correct": False, "tags": {"pola": ["Y"]}},   # Y baru: 0/0 → 0/1
    ]}
    rows, after = kb.session_deltas(baseline, [], session)
    d = {r["tag"]: r for r in rows}
    assert d["X"]["before"][:2] == (5, 7) and d["X"]["after"][:2] == (6, 8)
    assert d["Y"]["before"][:2] == (0, 0) and d["Y"]["after"][:2] == (0, 1)
    assert after["pola"]["X"] == {"benar": 6, "total": 8}
    # PURE: baseline tak termutasi
    assert baseline["quiz"]["pola"]["X"] == {"benar": 5, "total": 7}


def test_render_golden():
    """Idempoten: render(baseline, attempts nyata) == file tracker saat ini."""
    baseline = kb.load_baseline()
    attempts = kb.load_attempts()
    with open(kb.EVAL_PATH, encoding="utf-8") as f:
        eval_txt = f.read()
    with open(kb.JLPT_PATH, encoding="utf-8") as f:
        jlpt_txt = f.read()
    q_sess = [s for s in attempts if s.get("kind") == "quiz"]
    j_sess = [s for s in attempts if s.get("kind") == "jlpt"]
    q_date = q_sess[-1]["date"] if q_sess else None
    j_date = j_sess[-1]["date"] if j_sess else None
    q_sesi = baseline.get("meta", {}).get("quiz_sesi", 0) + len(q_sess)
    j_sesi = baseline.get("meta", {}).get("jlpt_sesi", 0) + len(j_sess)
    e = kb.render_evaluation(eval_txt, kb.aggregate(baseline, attempts, "quiz"), q_date, q_sesi)
    j = kb.render_jlpt(jlpt_txt, kb.aggregate(baseline, attempts, "jlpt"), j_date, j_sesi)
    assert e == eval_txt, "render_evaluation tak idempoten vs file saat ini"
    assert j == jlpt_txt, "render_jlpt tak idempoten vs file saat ini"


def run():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print(f"  ok  {t.__name__}")
    print(f"\n✅ {len(tests)} test lulus")


if __name__ == "__main__":
    run()
