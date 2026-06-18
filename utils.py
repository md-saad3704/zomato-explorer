# Helper utility functions

def format_currency(value):
    """
    Format currency values.
    """

    return f"₹{int(value):,}"


def format_number(value):
    """
    Format large numbers.
    """

    return f"{value:,}"



def apply_space_theme(fig):

    fig.update_layout(

        paper_bgcolor="#000008",
        plot_bgcolor="#000008",

        font=dict(
            family="Exo 2",
            color="#E8E8FF"
        ),

        title_font=dict(
            family="Orbitron",
            color="#00D4FF",
            size=20
        ),

        xaxis=dict(
            gridcolor="#1A1A3E",
            zerolinecolor="#1A1A3E"
        ),

        yaxis=dict(
            gridcolor="#1A1A3E",
            zerolinecolor="#1A1A3E"
        ),

        hoverlabel=dict(
            bgcolor="#0A0A1A",
            bordercolor="#00D4FF",
            font_color="#E8E8FF"
        )
    )

    return fig