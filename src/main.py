x = 1
y = 2

UIML = """
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title label="Liger Frontend" />
        <link href="css/style.css" rel="stylesheet" />
    </head>
    <box>
        <!-- Inputs -->
        <autocomplete />
        <button />
        <group-button />
        <checkbox />
        <radio />
        <input />
        <text-area />
        <select />
        <slider />
        <switch />

        <!-- Data Display -->
        <avatar />
        <badge />
        <chart />
        <chip />
        <grid />
        <list />
        <table />
        <tooltip />
        <tree />
        <progress />

        <!-- Feedback -->
        <alert />
        <dialog />
        <snackbar />
        <toast />

        <!-- Surface -->
        <accordion />
        <app-bar />

        <-- Built-in -->
        <color-picker />
        <audio-player />
        <video-player />
        <text-editor />
        <paint />
        <document-viewer />

        <!-- Navigation -->
        <drawer />
        <navigation />
        
        

        <text label="Hello, World!" />
        <p label="Hello, World!" />
        <ver></ver>
        <hor></hor>


        if x == 1:
            <text label="x = 1" />
        elif x == 2:
            <text label="x = 2" />
        else:
            <text label="other" />

        for i in range(10):
            <text label="Hello, World!" />
    </box>
"""
