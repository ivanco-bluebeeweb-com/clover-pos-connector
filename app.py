"""Extension declaration, capabilities, health check for Clover POS Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "clover-pos-connector",
    version="0.1.0",
    display_name="Clover POS",
    icon="icon.svg",
    capabilities=["clover_pos:manage"],
    description="Official Imperal connector for Clover POS (C30. Email Marketing & Newsletter). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("clover_pos_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} Clover POS connection(s) configured." if count else "Not connected yet."
    }
