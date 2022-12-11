"""The Hello Domain Integration."""

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Test."""
    hass.states.async_set("hello_domain.world", "Marcel")

    # Return boolean to indicate that initialization was successful.
    return True
