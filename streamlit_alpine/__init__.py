import os
import streamlit.components.v1 as components

component_dir = os.path.dirname(os.path.abspath(__file__))
_component_func = components.declare_component("streamlit_alpine", path=component_dir)

# To use with Live Server for development (DO NOT release your component with this, use the above for production releases)
# _component_func = components.declare_component("streamlit_alpine", url="http://127.0.0.1:5500/--TODO - update path to your project--/streamlit_alpine/streamlit_alpine/index.html")

# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def streamlit_alpine(name, key=None):
    """Create a new instance of "streamlit_alpine".

    Parameters
    ----------
    name: str
        The name of the thing we're saying hello to. The component will display
        the text "Hello, {name}!"
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    int
        The number of times the component's "Increment Clicks" button has been clicked.
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(name=name, key=key, default=0)

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value