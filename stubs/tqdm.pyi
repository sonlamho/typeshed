# Type stub file for tqdm
import io
from typing import Any, Callable, Iterable, Mapping, Optional, Tuple, Union

class tqdm(object):

    # methods from Comparable
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    # end of methods from Comparable
    monitor_interval: int = ...
    monitor: Optional[int] = ...
    @staticmethod
    def format_sizeof(num: float, suffix: str = ..., divisor: float = ...) -> str: ...
    @staticmethod
    def format_interval(t: int) -> str: ...
    @staticmethod
    def format_num(n: int) -> str: ...
    @staticmethod
    def ema(x: float, mu: float = ..., alpha: float = ...) -> float: ...
    @staticmethod
    def status_printer(file: io.TextIOWrapper) -> Callable: ...
    @staticmethod
    def format_meter(
        n: float,
        total: float,
        elapsed: float,
        ncols: Optional[int] = ...,
        prefix: str = ...,
        ascii: Union[bool, str] = ...,
        unit: str = ...,
        unit_scale: Union[bool, int, float] = ...,
        rate: Optional[float] = ...,
        bar_format: Optional[str] = ...,
        postfix: Any = ...,
        unit_divisor: float = ...,
        **extra_kwargs,
    ): ...
    @classmethod
    def write(cls, s: str, file: Optional[io.TextIOWrapper] = ..., end: str = ..., nolock: str = ...): ...
    def __init__(
        self,
        iterable: Optional[Iterable] = ...,
        desc: Optional[str] = ...,
        total: Optional[float] = ...,
        leave: bool = ...,
        file: Optional[Union[io.TextIOWrapper, io.StringIO]] = ...,
        ncols: Optional[int] = ...,
        mininterval: float = ...,
        maxinterval: float = ...,
        miniters: Optional[float] = ...,
        ascii: Optional[Union[str, bool]] = ...,
        disable: bool = ...,
        unit: str = ...,
        unit_scale: Union[bool, int, float] = ...,
        dynamic_ncols: bool = ...,
        smoothing: float = ...,
        bar_format: str = ...,
        initial: float = ...,
        position: Optional[int] = ...,
        postfix: Optional[Mapping] = ...,
        unit_divisor: float = ...,
        write_bytes: Optional[bool] = ...,
        lock_args: Optional[Tuple] = ...,
        nrows: Optional[int] = ...,
        gui: Optional[bool] = ...,
        **kwargs,
    ): ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback): ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __iter__(self): ...
    def update(self, n: int = ...): ...
    def close(self): ...
    def clear(self, nolock: bool = ...): ...
    def refresh(self, nolock: bool = ..., lock_args: Optional[Tuple] = ...): ...
    def unpause(self): ...
    def reset(self, total: Optional[float] = ...): ...
    def set_description(
        self,
        desc: Optional[str] = ...,
        refresh: bool = ...,
    ): ...
    def set_description_str(
        self,
        desc: Optional[str] = ...,
        refresh: bool = ...,
    ): ...
    def set_postfix(self, ordered_dict: Optional[Mapping] = ..., refresh: bool = ..., **kwargs): ...
    def set_postfix_str(self, s: str = ..., refresh: bool = ...): ...
    @property
    def format_dict(self) -> Mapping: ...
    def display(self, msg: Optional[str] = ..., pos: Optional[int] = ...): ...
    @classmethod
    def wrapattr(
        cls,
        stream,
        method: str,
        total: Optional[float] = ...,
        bytes: bool = ...,
        **tqdm_kwargs,
    ) -> io.TextIOWrapper: ...

def trange(*args, **kwargs) -> tqdm: ...
