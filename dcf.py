from typing import Dict, List, Optional


def calculate_dcf(
    revenue: float,
    growth_rate: float,
    discount_rate: float,
    years: int,
) -> Dict[str, Optional[object]]:
    if revenue <= 0 or growth_rate < 0 or discount_rate <= 0 or years <= 0:
        raise ValueError("All inputs must be positive numbers and years must be greater than 0.")

    yearly_cash_flow_data: List[Dict[str, float]] = []
    discounted_cash_flows: List[float] = []

    for year in range(1, years + 1):
        projected_cash_flow = revenue * ((1 + growth_rate) ** (year - 1))
        discounted_cash_flow = projected_cash_flow / ((1 + discount_rate) ** year)

        yearly_cash_flow_data.append(
            {
                "year": year,
                "projected_cash_flow": round(projected_cash_flow, 2),
                "discounted_cash_flow": round(discounted_cash_flow, 2),
            }
        )
        discounted_cash_flows.append(discounted_cash_flow)

    final_valuation = round(sum(discounted_cash_flows), 2)
    terminal_value: Optional[float] = None
    discounted_terminal_value: Optional[float] = None
    total_valuation_with_terminal: Optional[float] = None

    if discount_rate > growth_rate:
        last_cash_flow = yearly_cash_flow_data[-1]["projected_cash_flow"]
        terminal_value = round(
            last_cash_flow * (1 + growth_rate) / (discount_rate - growth_rate), 2
        )
        discounted_terminal_value = round(
            terminal_value / ((1 + discount_rate) ** years), 2
        )
        total_valuation_with_terminal = round(
            final_valuation + discounted_terminal_value,
            2,
        )

    return {
        "yearly_cash_flows": yearly_cash_flow_data,
        "final_valuation": final_valuation,
        "terminal_value": terminal_value,
        "discounted_terminal_value": discounted_terminal_value,
        "total_valuation_with_terminal": total_valuation_with_terminal,
    }
