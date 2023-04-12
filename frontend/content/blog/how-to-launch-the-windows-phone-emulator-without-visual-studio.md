---
title: How to launch the Windows Phone Emulator without Visual Studio
description: 
date_created: 2013-08-13
---

Here's a simple trick that lets you launch the Windows Phone 8 Emulator without using Visual Studio 2012.

It's quite simple:

Open "Command Prompt" in Administrator mode (right click on it on the Start page icon, choose *Run as administrator*)

Launch the emulator using the following command (with quotes): `"C:\Program Files (x86)\Microsoft XDE\8.0\xde" -vhd "C:\Program Files (x86)\Microsoft SDKs\Windows Phone\v8.0\Emulation\Images\Flash.vhd"`

This will launch the Windows Phone emulator so you can easily test you mobile website without going through Visual Studio. As a rule of thumb, Internet Explorer for Windows Phone behaves like its desktop counterpart, but you should still test it just to be sure.

