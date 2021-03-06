#-------------------------------------------------
#
# Project created by QtCreator 2011-12-26T20:42:08
#
#-------------------------------------------------

QT       += core gui opengl network
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets


PROJECT(muView)




SET(DESTDIR     ../../bin)
SET(OBJECTS_DIR ../../bin/build/$$TARGET/.obj)
SET(MOC_DIR     ../../bin/build/$$TARGET/.moc)
SET(RCC_DIR     ../../bin/build/$$TARGET/.rcc)
SET(UI_DIR      ../../bin/build/$$TARGET/.ui)



LIBS += -L../../bin/libs
LIBS += -L../../../Common/shogun/src/shogun
LIBS += -lcommon
LIBS += -ldata

# glew for windows
win32 {
    LIBS += -lglew32
    QMAKE_CXXFLAGS += -openmp
    DEFINES += _CRT_SECURE_NO_WARNINGS
    LIBS += "/nodefaultlib:libcmt"
}
unix {
    QMAKE_CXXFLAGS  += -fopenmp
    LIBS += -lgomp
    LIBS += -lshogun
}


INCLUDEPATH += ../../include
INCLUDEPATH += ../../../Common/include
INCLUDEPATH += ../../../Common/shogun/src
INCLUDEPATH += ../../../Common/drl/drl
INCLUDEPATH += .
INCLUDEPATH += ../


SOURCES += \
    ../../src/muView/HeartMainWindow.cpp \
    ../../src/muView/HeartMain.cpp \
    ../../src/muView/Histogram.cpp \
    ../../src/muView/VolumeRenderer.cpp \
    ../../src/muView/VoxelAssociativity.cpp \
    ../../src/muView/RenderEngine.cpp \
    ../../src/muView/ParallelCoordinates.cpp \
    ../../src/muView/HeartDock.cpp \
    ../../src/muView/RenderEngine3D.cpp \
    ../../src/muView/RenderEngine2D.cpp \
    ../../src/Shogun_Wrapper.cpp \
    ../../src/DRL_Wrapper.cpp \
    ../../src/DimensionalityReductionThreaded.cpp \
    ../../src/DimensionalityReduction.cpp \
    ../../src/muView/PCAView.cpp


HEADERS  += \
    ../../include/muView/HeartMainWindow.h \
    ../../include/muView/Histogram.h \
    ../../include/muView/VolumeRenderer.h \
    ../../include/muView/VoxelAssociativity.h \
    ../../include/muView/RenderEngine.h \
    ../../include/muView/ParallelCoordinates.h \
    ../../include/muView/HeartDock.h \
    ../../include/muView/RenderEngine3D.h \
    ../../include/muView/RenderEngine2D.h \
    ../../include/Shogun_Wrapper.h \
    ../../include/DRL_Wrapper.h \
    ../../include/DimensionalityReductionThreaded.h \
    ../../include/DimensionalityReduction.h \
    ../../include/muView/PCAView.h


RESOURCES += \
    ../../../Common/fonts/arial.qrc

ADD_EXECUTABLE(muView muView_sources)
