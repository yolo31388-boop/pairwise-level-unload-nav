import pytest
import gameplay.level_unload_nav as mod

CASES = [
    ("ref_count", (1, 2)),
    ("load_barrier", (1, 2)),
    ("nav_rebuild", (1, 2)),
    ("stale_object", (1, 2)),
    ("scene_switch", (1, 2)),
    ("async_join", (1, 2)),
    ("obstacle_clear", (1, 2)),
    ("npc_stuck", (1, 2)),
    ("tile_release", (1, 2)),
    ("validation", (1, 2)),
    ("barrier_timeout", (1, 2)),
    ("fallback_nav", (1, 2)),
    ("memory_check", (1, 2)),
    ("stuck_metric", (1.0, 2.0)),
    ("batch_guard", (1, 2)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
