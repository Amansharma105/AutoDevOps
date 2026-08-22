class ConfigSummary:
    """Create a simple summary of infrastructure configuration."""

    def create(self, config):
        resources = config.get("resources", [])

        summary = {
            "total_resources": len(resources),
            "resource_types": {},
            "providers": {}
        }

        for resource in resources:
            resource_type = resource.get("type", "unknown")
            provider = resource.get("provider", "unknown")

            summary["resource_types"][resource_type] = (
                summary["resource_types"].get(resource_type, 0) + 1
            )

            summary["providers"][provider] = (
                summary["providers"].get(provider, 0) + 1
            )

        return summary
