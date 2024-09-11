# AutoTabClose
AutoTabClose is a simple plugin for Sublime Text designed to automatically closing tabs with a certain prefix.

This is useful when you have tabs of a transient nature (sometimes created by other plugins) that you want to be able to access, but don't neccesairly want to appear in searches/file navigation. Any that match the given prefix will be close automatically when the tab becomes inactive.

# Installation

1. Install the Sublime Text Package Control plugin if you don't have it already.
1. Open the command palette and start typing `Package Control: Install Package`.
1. Enter `AutoTabClose`

# Configuration

The settings are incredibly simple, at present this plugin supports a single setting called prefixes. An example set-up might look like this:

```
{
    "prefixes": ["INLINE:"]
}
```

This will automatically close any tab that begins with the name "INLINE:" when that tab becomes deactivated.
