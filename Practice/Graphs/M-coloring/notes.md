# M-coloring

**Type:** Practice / Standalone
**Language:** python3
**Date:** 18/06/2026

---

End the recursion when we reach the last vertex because we reached it only when we were able to find a valid color for it till the end. otherwise we would have returned false early. Time complexity is O(v*m^v) and space is O(v+e) where m=number of colors. v= number of vertices. and we are multiplying by v because of the cancolor function.