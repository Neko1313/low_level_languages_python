import time
import tracemalloc
from typing import Callable, TypeVar, Any
from loguru import logger
from functools import wraps
import os
import json

T = TypeVar("T", bound=Callable[..., Any])


def measure_performance(func: T) -> T:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        log_file = f"log/{func.__name__}_log.log"
        json_file = f"log/{func.__name__}_data.json"

        logger.add(log_file, rotation="1024 MB")

        tracemalloc.start()
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        execution_time = end_time - start_time
        memory_used = current / 1024
        peak_memory = peak / 1024

        logger.info(
            f"Function {func.__name__} executed in {execution_time:.4f} seconds"
        )
        logger.info(
            f"Memory used: {memory_used:.2f} KB, Peak memory: {peak_memory:.2f} KB"
        )

        performance_data = {
            "function": func.__name__,
            "execution_time": execution_time,
            "memory_used": memory_used,
            "peak_memory": peak_memory,
            "len": len(result),
        }

        os.makedirs("log", exist_ok=True)
        if os.path.exists(json_file):
            with open(json_file, "r+") as file:
                data = json.load(file)
                data.append(performance_data)
                file.seek(0)
                json.dump(data, file, indent=4)
        else:
            with open(json_file, "w") as file:
                json.dump([performance_data], file, indent=4)

        return result  # type: ignore

    return wrapper  # type: ignore
