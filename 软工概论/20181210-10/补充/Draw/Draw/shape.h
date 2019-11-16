#include "screen.h"

#ifndef SHAPE_H
#define SHAPE_H


class Shape
{
	Point center;
	int color;
	int angle;
	virtual void drawShape()=0;
public:
	Shape(Point p)
		:center(p),
		color(screen.foreground()),angle(0){}
	int getColor() {return color;}
	void setColor(int c){color=c;}
	int getAngle(){return angle;}
	void setAngle(int a){angle=a;}
	Point position(){return center;}
	void moveTo(Point p){center=p;}

	void draw()
	{
	  int saveColor=screen.foreground();
	  screen.foreground(getColor());
	  drawShape();
	  screen.foreground(saveColor);
	}

	void hide()
	{
		int saveColor=screen.foreground();
	  screen.foreground(screen.background());
	  drawShape();
	  screen.foreground(saveColor);
	}
	void rotate(int angle)
	{
	  setAngle(getAngle()+angle);
	  draw();
	}
};
#endif