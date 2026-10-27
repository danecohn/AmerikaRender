# Generated Blender assets

Generate the theme and startup template using checksum-pinned Blender 5.0.1, the supported major baseline, in isolated CI resources. The new factory template uses the Vigil Render workspace. Existing user files retain their Render/Amerika workspace instead of being renamed. Add-on/operator IDs, paths, launcher names and update channels remain unchanged.

The GUI generator runs under Xvfb with a temporary BLENDER_USER_CONFIG and XDG/project roots. It never writes the developer's normal Blender startup/preferences. The workflow generates XML, startup.blend and a screenshot; it then reopens the saved file in Blender and asserts the branded workspace. Actual Blender tool tests use the pinned binary. Merge the generated assets only after these checks pass. Original logos, splash artwork and four asset repositories are unchanged.

Real Blender CI run 40498411918 passed all 19 tests and generated/reopened the startup. Review found the initial screenshot was black and the panel poll still matched only the old workspace. The follow-up retains legacy names in the poll, includes Vigil Render, forces a completed redraw before capture, and rejects blank screenshots. Generated outputs will be committed only after that visual check passes.
