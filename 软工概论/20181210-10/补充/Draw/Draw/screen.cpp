#include <stdlib.h>
#include <stdio.h>
#include "screen.h"

#define VIRTUAL_MAXX 100
#define VIRTUAL_MAXY 100



Point Screen::translate(Point p)
{
	//coordinate range:0,0 to maxX,maxY
	int x=translateX(p.x());
	int y=translateY(p.y());
	return Point(x,y);
}

int Screen::translateX(int x)
{
	return int(long(maxX)*long(x)/VIRTUAL_MAXX);
}

int Screen::translateY(int y)
{
	return maxY-int(long(maxY)*long(y)/VIRTUAL_MAXY);
}

void Screen::initalize(HWND hWnd,HDC hDc)
{
	hWindow=hWnd;
	hDeviceContext=hDc;
	RECT aRect;
	GetClientRect(hWnd,&aRect);
	maxX=aRect.right;
	maxY=aRect.bottom;
}

void Screen::cleanup()
{
	 hWindow=NULL;
	 hDeviceContext=NULL;
     maxX=maxY=0;
}

void Screen::moveTo(Point p)
{
    if(hWindow==NULL)
		return;
	p=translate(p);
	MoveToEx(hDeviceContext,p.x(),p.y(),NULL);
	
}

void Screen::lineTo(Point p)
{
  if(hWindow==NULL)
		return;
	p=translate(p);
	LineTo(hDeviceContext,p.x(),p.y());
}

void Screen::circle(Point p,int radius)
{
	if(hWindow==NULL)
		return;
	p=translate(p);

	int xr=long(maxX)*long(radius)/VIRTUAL_MAXX;
	int yr=long(maxY)*long(radius)/VIRTUAL_MAXY;
	radius=(xr+yr)/2;
	Ellipse(hDeviceContext,p.x()-radius,p.y()-radius,p.x()+radius,p.y()+radius);
}

void Screen::background(int color)
{
     //setbakcolor(color);
}

int Screen::background()
{
    return 0;
}

void Screen::foreground(int color)
{
	//setcolor(color);
} 

int Screen::foreground()
{
   return 0;
}

void Screen::clear()
{
	//cleardevice();
}


Screen screen;