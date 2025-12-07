#!/usr/bin/env python3
"""Skills system agent with built-in skills.

Lab 2.3 Deliverable: Demonstrates adding built-in skills (datetime, math)
with configuration options.
"""

from signalwire_agents import AgentBase


class SkillsAgent(AgentBase):
    """Agent with built-in skills for various capabilities."""

    def __init__(self):
        super().__init__(name="skills-agent")

        self.prompt_add_section(
            "Role",
            "You are a helpful assistant with access to various skills. "
            "Use your skills to help users with time and math calculations."
        )

        self.prompt_add_section(
            "Capabilities",
            bullets=[
                "Tell the current date and time in various timezones",
                "Perform mathematical calculations"
            ]
        )

        self.add_language("English", "en-US", "rime.spore")

        # Add built-in skills
        self._setup_skills()

    def _setup_skills(self):
        """Configure built-in skills."""

        # DateTime skill with timezone configuration
        self.add_skill(
            "datetime",
            {
                "timezone": "America/New_York",
                "format": "12-hour"
            }
        )

        # Math skill (no special configuration needed)
        self.add_skill("math")


class MultiTimezoneAgent(AgentBase):
    """Challenge extension: Agent that handles multiple timezone queries.

    Note: The datetime skill provides a single get_datetime function.
    To handle multiple timezones, we configure a default timezone and
    provide instructions for the AI to handle timezone conversion requests.
    """

    def __init__(self):
        super().__init__(name="multi-timezone-agent")

        self.prompt_add_section(
            "Role",
            "You help users check time in different timezones."
        )

        self.prompt_add_section(
            "Timezone Information",
            bullets=[
                "Eastern Time (ET): America/New_York",
                "Pacific Time (PT): America/Los_Angeles",
                "London (GMT/BST): Europe/London",
                "Tokyo (JST): Asia/Tokyo",
                "When users ask for time in a specific timezone, use the datetime skill and mention the timezone"
            ]
        )

        self.add_language("English", "en-US", "rime.spore")

        # Single datetime skill - the AI handles timezone context
        self.add_skill(
            "datetime",
            {
                "timezone": "America/New_York",
                "format": "12-hour"
            }
        )


if __name__ == "__main__":
    agent = SkillsAgent()
    agent.run()
