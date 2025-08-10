# Privacy

This Civic Transparency standard is built with **privacy by design**.

## Principles
1. **No personal data.** The system never publishes account IDs, handles, or message text.
2. **Bucketed fields.** Sensitive fields (e.g., account age) are provided in broad ranges.
3. **Aggregate-only outputs.** Metrics are computed over large groups.
4. **Minimum group sizes.** Outputs are only published when `k-anonymity ≥ 100`.
5. **No cross-platform joins.** Fields are designed to prevent linking to other datasets.

## Safeguards
- Suppression of small-cell counts.
- Public outputs are decoupled from raw post logs.
- Provenance tags are only used internally to compute metrics, not displayed for individual posts.

## Compliance
- Compatible with privacy regulations such as GDPR and CCPA.
- Meets transparency obligations in laws like the EU Digital Services Act without exposing personal data.
