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

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Exo 2",
            color="#E8E8FF",
            size=13
        ),

        xaxis=dict(
            showgrid=True,
            gridcolor="rgba(26,26,62,0.20)",
            zeroline=False,
            showline=False,
            tickfont=dict(color="#E8E8FF")
        ),

        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(26,26,62,0.20)",
            zeroline=False,
            showline=False,
            tickfont=dict(color="#E8E8FF")
        ),

        hoverlabel=dict(
            bgcolor="#0A0A1A",
            bordercolor="#00D4FF",
            font=dict(
                family="Exo 2",
                color="#E8E8FF"
            )
        ),

        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),

        showlegend=False
    )

    fig.update_traces(
    marker_color="#00D4FF",
    marker_line_color="#7B2FBE",
    marker_line_width=1.5,
    opacity=0.95
)

    return fig