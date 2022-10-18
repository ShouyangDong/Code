import tvm
from tvm.script import tir as T


def matmul(
    a: T.handle, b: T.handle, c: T.handle
) -> None:  # pylint: disable=no-self-argument
    T.func_attr({"global_symbol": "matmul", "tir.noalias": True})
    A = T.match_buffer(a, (1024, 1024), "float32")
    B = T.match_buffer(b, (1024, 1024), "float32")
    C = T.match_buffer(c, (1024, 1024), "float32")
    for i, j, k in T.grid(1024, 1024, 1024):
        with T.block("matmul"):
            vi, vj, vk = T.axis.remap("SSR", [i, j, k])
            with T.init():
                C[vi, vj] = 0.0
            C[vi, vj] = C[vi, vj] + A[vi, vk] * B[vk, vj]


def test_func():
    func = T.prim_func(matmul)


if __name__ == "__main__":
    test_func()
