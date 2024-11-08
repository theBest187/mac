
cmake_minimum_required(VERSION 3.15)

project(MyIOSApp)

set(CMAKE_SYSTEM_NAME iOS)
set(CMAKE_OSX_ARCHITECTURES "arm64")
set(CMAKE_OSX_DEPLOYMENT_TARGET "12.0")

add_executable(MyIOSApp src/iOS/Info.plist src/iOS/DummyClass.h src/iOS/main.cpp src/iOS/Test.mp3 src/iOS/DummyClass.m src/iOS/Info.plist src/iOS/DummyClass.h src/iOS/main.cpp src/iOS/Test.mp3 src/iOS/DummyClass.m src/iOS/Info.plist src/iOS/DummyClass.h src/iOS/main.cpp src/iOS/Test.mp3 src/iOS/DummyClass.m src/iOS/Info.plist src/iOS/DummyClass.h src/iOS/main.cpp src/iOS/Test.mp3 src/iOS/DummyClass.m src/iOS/Info.plist src/iOS/DummyClass.h src/iOS/main.cpp src/iOS/Test.mp3 src/iOS/DummyClass.m src/iOS/Info.plist src/iOS/DummyClass.h src/iOS/main.cpp src/iOS/Test.mp3 src/iOS/DummyClass.m src/iOS/Info.plist src/iOS/DummyClass.h src/iOS/main.cpp src/iOS/Test.mp3 src/iOS/DummyClass.m src/iOS/Info.plist src/iOS/DummyClass.h src/iOS/main.cpp src/iOS/Test.mp3 src/iOS/DummyClass.m src/iOS/Info.plist src/iOS/DummyClass.h src/iOS/main.cpp src/iOS/Test.mp3 src/iOS/DummyClass.m src/iOS/Info.plist src/iOS/DummyClass.h src/iOS/main.cpp src/iOS/Test.mp3 src/iOS/DummyClass.m)

target_link_libraries(MyIOSApp UIKit Foundation)
    