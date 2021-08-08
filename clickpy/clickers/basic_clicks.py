"""Starter Clicking Strategies."""

from dataclasses import dataclass
from random import randint
from time import sleep
from typing import Optional

import pyautogui


@dataclass
class BasicRandomClickStrategy:
    """The first random clicking strategy I came up with."""

    min_sleep_time: int = 1
    max_sleep_time: int = 180
    sleep_time: Optional[int] = None
    print_debug: Optional[bool] = None

    def click(self) -> None:
        """SupportsClick Protocol method.

        Either use the sleep_time passed into the ctr, or get a random int
        between min_sleep_time and max_sleep_time."""
        timer = (
            self.sleep_time
            if self.sleep_time
            else randint(self.min_sleep_time, self.max_sleep_time)
        )

        if self.print_debug:
            print(f"Random thread sleep for {timer} seconds.")

        sleep(timer)

        pyautogui.click()

        if self.print_debug:
            print("Clicked")


@dataclass
class FastClickStrategy:
    """Fast Clicking Strategy."""

    sleep_time = 1
    print_debug: Optional[bool] = None

    def click(self) -> None:
        """SupportsClick Protocol method.

        Defaults to 1 second sleep time, or whatever value is passed in from ctr.
        """
        sleep(self.sleep_time)

        if self.print_debug:
            print("Thread sleep for 1 second.")

        pyautogui.click()

        if self.print_debug:
            print("Clicked!")
