import cx_Freeze

executables = [
    cx_Freeze.Executable(script="main.py", icon="Recursos/icone.ico")
]

cx_Freeze.setup(
    name="WACKY-RACES",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["Recursos", "ReadMe.md"],
        }
    },
    executables=executables,
)

 