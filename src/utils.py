import time
import tracemalloc
from typing import Callable, TypeVar, Any
from loguru import logger
from functools import wraps

T = TypeVar('T', bound=Callable[..., Any])

def measure_performance(func: T) -> T:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        log_file = f"log/{func.__name__}_log.log"
        logger.add(log_file, rotation="10 MB")

        tracemalloc.start()
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        execution_time = end_time - start_time
        memory_used = current / 1024
        peak_memory = peak / 1024
        logger.info(f"Function {func.__name__} executed in {execution_time:.4f} seconds")
        logger.info(f"Memory used: {memory_used:.2f} KB, Peak memory: {peak_memory:.2f} KB")

        return result # type: ignore
    return wrapper  # type: ignore
