#include <math.h>
#ifndef M_PI
#define M_PI 3.1415
#endif

#include "point.h"
#include "shape.h"
typedef Shape * ShapePointer;//定义Shape型指针变量
void rotateArray(ShapePointer array[],int size);
void far pascal rotateShapes();

Point rotateAboutOrigin(Point p,int angle)
{
  double theta=angle*M_PI/180;
  double cos_theta=cos(theta);
  double sin_theta=sin(theta);
  int x=(int)(p.x()*cos_theta-p.y()*sin_theta);
  int y=(int)(p.x()*sin_theta+p.y()*cos_theta);
  return  Point(x,y);
}

////////////////////////////////////////////////////////
//class Circle
////////////////////////////////////////////////////////
class Circle:public Shape
{
  int radius;
  void drawShape()
  {
     Point ctr=rotateAboutOrigin(position(),getAngle());
	 screen.circle(ctr,radius);
  }
public:
	Circle(Point p,int r)
		:Shape(p),radius(r){}
};


////////////////////////////////////////////////////////
//class Rectangle
////////////////////////////////////////////////////////
class Rectangle1:public Shape//本来使用的是Rectangle可是和系统的冲突只能改名了
{
  virtual void drawShape()
  {
	  Point a(position()-(extent/2));
	  Point c(a+extent);
	  Point b(c.x(),a.y());
	  Point d(a.x(),c.y());

	  a=rotateAboutOrigin(a,getAngle());
	  b=rotateAboutOrigin(b,getAngle());
	  c=rotateAboutOrigin(c,getAngle());
	  d=rotateAboutOrigin(d,getAngle());

	  screen.moveTo(a);
	  screen.lineTo(b);
	  screen.lineTo(c);
	  screen.lineTo(d);
	  screen.lineTo(a);
  }
protected:
	Point extent;
public:
	Rectangle1(Point ctr,Point ext)
		:Shape(ctr),extent(ext){}
};

////////////////////////////////////////////////////////
//class Triangle
////////////////////////////////////////////////////////
class Triangle:public Rectangle1
{
	virtual void drawShape()
	{
	  int w2=extent.x()/2;//一半宽
	  int h2=extent.y()/2;//一半高
	  Point a(position()+Point(0,h2));
	  Point b(position()+Point(w2,-h2));
	  Point c(position()+Point(-w2,-h2));

	  a=rotateAboutOrigin(a,getAngle());
	  b=rotateAboutOrigin(b,getAngle());
	  c=rotateAboutOrigin(c,getAngle());

	  screen.moveTo(a);
	  screen.lineTo(b);
	  screen.lineTo(c);
	  screen.lineTo(a);
	}
public:
	Triangle(Point ctr,Point ext)
		:Rectangle1(ctr,ext){}
};

void rotateArray(ShapePointer array[],int size)
{
   for(int j=0;j<size;j++)
   {
		array[j]->draw();
		for(int i=0;i<8;i++)//每个形状旋转8次
		{
			array[j]->rotate(10);//每个不同的形状调用自己的rotate（）方法
		}
   }
}
void far pascal rotateShapes()
{
	ShapePointer shapeArray[10];
	int size=0;

	shapeArray[size++] = new Circle  (Point(60,6),4);
	shapeArray[size++] = new Rectangle1  (Point(70,6),Point(8,8));
	shapeArray[size++] = new Triangle  (Point(80,6),Point(8,8));

	rotateArray(shapeArray,size);

}
 