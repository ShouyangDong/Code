from transform import prim_func
from .transform import tir as T



def mma_desc(a: T.handle, b: T.handle, c: T.handle) -> None:
    A = T.match_buffer(a, (16, 16), align=64, offset_factor=1)
    B = T.match_buffer(b, (16, 16), align=64, offset_factor=1)
    C = T.match_buffer(c, (16, 16), align=64, offset_factor=1)

    with T.block("root"):
        T.reads(C[0 : 16, 0 : 16], A[0 : 16, 0 : 16], B[0 : 16, 0 : 16])
        T.writes(C[0 : 16, 0 : 16])
        for i, j, k in T.grid(16, 16, 16):
            with T.block("update"):
                vii, vjj, vkk = T.axis.remap("SSR", [i, j, k])
                C[vii, vjj] = C[vii, vjj] + A[vii, vkk] * B[vjj, vkk]


def test_func():
    func = t.prim_func(mma_desc)

if __name__ == "__main__":
    test_func()
