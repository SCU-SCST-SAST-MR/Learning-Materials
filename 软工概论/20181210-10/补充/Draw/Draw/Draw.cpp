#include <windows.h>
#include "screen.h"
#include "shape.h"



CHAR szTitle[]="C++ MS Windows Rotate Shapes";
CHAR szWindowClass[]="EX0101";
BOOL MyRegisterClass(HINSTANCE hInstance);
BOOL InitInstance(HINSTANCE,int);
LRESULT CALLBACK WndProc(HWND,UINT,WPARAM,LPARAM);
void MyPrint(HWND hWnd);
int CALLBACK WinMain(HINSTANCE hInstance,HINSTANCE hPreInstance,LPTSTR lpCmdLine,int nCmdShow)
{
	MSG msg;
	MyRegisterClass(hInstance);
	if(!InitInstance(hInstance,nCmdShow))
	{
	  return FALSE;
	}
	while (GetMessage(&msg,NULL,0,0))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}
	return (int) msg.wParam;
}
BOOL MyRegisterClass(HINSTANCE hInstance)
{
	WNDCLASSEX wcex;
	wcex.cbSize=sizeof(WNDCLASSEX);
	wcex.style=CS_HREDRAW|CS_VREDRAW;
	wcex.lpfnWndProc=(WNDPROC)WndProc;
	wcex.cbClsExtra=0;
	wcex.cbWndExtra=0;
	wcex.hInstance=hInstance;
	wcex.hIcon=NULL;
	wcex.hCursor=NULL;
	wcex.hbrBackground=(HBRUSH)(COLOR_WINDOW+1);
	wcex.lpszMenuName=NULL;
	wcex.lpszClassName=szWindowClass;
	wcex.hIconSm=NULL;
	return RegisterClassEx(&wcex);
}
BOOL InitInstance(HINSTANCE hInstance,int nCmdShow)
{
	HWND hWnd=CreateWindow(szWindowClass,szTitle,WS_OVERLAPPEDWINDOW,CW_USEDEFAULT,CW_USEDEFAULT,CW_USEDEFAULT,CW_USEDEFAULT,NULL,NULL,hInstance,NULL);
	if(!hWnd)
	{
		return FALSE;
	}
	ShowWindow(hWnd,nCmdShow);
	UpdateWindow(hWnd);//send WM_PAINT message
	InvalidateRect(hWnd,NULL,TRUE);
	return TRUE;
}
LRESULT CALLBACK WndProc(HWND hWnd,UINT message,WPARAM wParam,LPARAM lParam)
{
	switch(message)
	{
	/*case WM_COMMAND:
		if(wParam==IDM_ABOUT)
		{
			FARPROC lpProcAbout=MakeProcInstance(About,screen.instance());
			DialogBox(screen.instance(),"AboutBox",hWnd,lpProcAbout);

			FreeProcInstance(lpProcAbout);
		}
		else
			return(DefWindowProc(hWnd,message,wParam,lParam))*/
	case WM_PAINT:
		MyPrint(hWnd);
		break;
	case WM_DESTROY:
		PostQuitMessage(0);
		break;
	default:
		return DefWindowProc(hWnd,message,wParam,lParam);
	}
	return 0;
}
void MyPrint(HWND hWnd)
{
	PAINTSTRUCT ps;
	HDC hdc;
    hdc=::BeginPaint(hWnd,&ps);
	char szBuf[100];
	strcpy(szBuf,"Well-designed class interface");
	::TextOut(hdc,10,4,szBuf,lstrlen(szBuf));
	strcpy(szBuf,"produce modular objects and");
	::TextOut(hdc,10,20,szBuf,lstrlen(szBuf));
	strcpy(szBuf,"replaceable system components");
	::TextOut(hdc,10,36,szBuf,lstrlen(szBuf));

	screen.initalize(hWnd,hdc);
	rotateShapes();//完成图形的旋转
	screen.cleanup();
	
	::EndPaint(hWnd,&ps);
}
