# pairwise-level-unload-nav

## 领域

游戏、图形与多媒体

## 主题

关卡卸载寻路

## 说明

引用计数、加载屏障与导航数据重建。

初始状态下 `gameplay/level_unload_nav.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
