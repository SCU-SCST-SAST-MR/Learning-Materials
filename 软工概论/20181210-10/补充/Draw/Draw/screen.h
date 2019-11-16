#ifndef SCREEN_H
#define SCREEN_H

#include "point.h"
#include "windows.h"
//////////////////////////////////////////////////////
//class Screen(interface)
//////////////////////////////////////////////////////

class Screen
{
	HWND hWindow;
	HDC hDeviceContext;
	HANDLE hCurrentInstance;
	
	int maxX;
	int maxY;
	Point translate(Point p);
	int translateX(int x);
	int translateY(int y);
public:
	Screen()
		:hWindow(NULL),
		hDeviceContext(NULL),
		hCurrentInstance(NULL),
		maxX(0),
		maxY(0)
	{}
	HANDLE instance()  {return hCurrentInstance;}
	void instance(HANDLE h) {hCurrentInstance = h;}
	
	enum{black,		blue,			green,		cyan,
		red,	    magenta,		brown,		lightgray,
		darkgray,   lightblue,		lightgreen,  lightcyan,
		lightred,	lightmagenta,	yellow,      white
	};
	void initalize(HWND hWnd,HDC hDC);
	void cleanup();
	void moveTo(Point p);
	void lineTo(Point p);
	void circle(Point p,int radius);
	void background(int color);
	int background();
	void foreground(int color);
	int foreground();
	void clear();
	
};
/////////////////////////////////////////////////////
//global screen object
//(only one instance ofScrenn allowed per program)
/////////////////////////////////////////////////////
extern Screen screen;

void far pascal rotateShapes();//define in rotate.cpp

#endif