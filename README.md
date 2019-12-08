X++ public beta source code. No sprites, music, etc. the MIT license only applies to my code. This is purely a fan project; I am **NOT** affiliated with Capcom. Full source tree will be pushed in January 2020, until then I might commit bits and pieces of related code here and there.

***

![Mega Man X++](https://i.imgur.com/HNAEqne.png)

Mega Man X++ is a free and open-source Mega Man X engine (fan project) and toolset written in C and Lua, focused on accuracy. You can create anything from a single level to a full, standalone fan game with it. Or just play Mega Man X levels until your eyes are bleed. I am not responsible if your eyes bleed. Think [Mega Man Maker](https://megamanmaker.com/), but more powerful: levels can include their own custom content. Both the C engine and Lua scripts are licensed under the MIT license.

* Compiles on Windows, macOS, and Linux/BSD.
* Play as X, with the same tight controls as the original. Or, create your own character.
* Dozens of built-in enemies, stage gimmicks and bosses from the SNES trilogy.
* Customizable level editor catering to both new and advanced users.
* Extensive, detailed documentation on how to use all parts of the engine and tools.
* Import objects, music, tilesets etc. into your level from inside the editor.
* Easily play and distribute levels using simple `zip` files.
* Clear levels in co-op mode in split-screen mode or online with a friend.

# Build and run
## macOS/Linux/BSD

First, ensure you have SDL2 and LuaJIT installed. Then, simply:

```
$ make
$ make run
```

## Windows

```
nmake -f Makefile.win
```

***

X++ is currently in a **beta** state. Not all of the above features are implemented yet.
