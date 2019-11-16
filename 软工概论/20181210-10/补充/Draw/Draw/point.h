#ifndef POINT_H
#define POINT_H

class Point
{
  int xVal;
  int yVal;
public:
	Point(){xVal=0;yVal=0;}
	Point(int x, int y){xVal=x;yVal=y;}
	int x() {return xVal;}
	int y() {return yVal;}
	Point operator+(Point p)
	{return Point(xVal+p.x(),yVal+p.y());}
	Point operator-(Point p)
	{return Point(xVal-p.x(),yVal-p.y());}
	Point operator * (int i)
	{return Point(xVal*i,yVal*i);}
	Point operator /(int i)
	{return Point(xVal/i,yVal/i);}
};

#endif