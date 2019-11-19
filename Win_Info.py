import pygetwindow as gw
class WinInfo():
    def __init__(self,*lst):
        self.window_name = 'Untitled' #WINDOW NAME '...'
        self.get_all_windows()
        self.get_all_titles()
        self.get_win_title(self.window_name)
        #self.maximize_win() # MAXIMIZE WINDOW
        #self.minimize_win() #MINIMIZE WINDOW
        #self.restore_win() #RESTORE WINDOW
        #self.resize_win(self.window_name,600,600)# RESIZE WINDOW
        #self.move_win(self.window_name,100,100)# MOVE WINDOW
        self.size_win(self.window_name)#SIZE WINDOW
        self.topleft_win(self.window_name)#TOP_LEFT WINDOW
        self.bottomright_win(self.window_name)#BOTTOM_RIGHT WINDOW
        self.width_win(self.window_name)#WIDTH WINDOW
        self.height_win(self.window_name)#HEIGHT WINDOW
        self.top_win(self.window_name)#TOP WINDOW
        self.left_win(self.window_name)#LEFT WINDOW
        #self.close('Untitled')#CLOSE WINDOW
    def get_all_windows(self):
        try:
            print(gw.getAllWindows(),'\n')
        except:
            print('...')
    def get_all_titles(self):
        try:
            print(gw.getAllTitles(),'\n')
        except:
            print('...')
    def get_win_title(self,title='Untitled'):
        try:
            window=gw.getWindowsWithTitle(title)[0]
            if window:
                print(title+' -> WINDOW NAME','\n')
            if not window:
                print(title+' -> WINDOW NAME(NOT EXIST)','\n')
        except:
            print('...')
    def maximize_win(self,title='Untitled'):
        try:
            notepadWindow = gw.getWindowsWithTitle(title)[0]
            notepadWindow.maximize()
            if notepadWindow.isMaximized:
                print(title+'  <-> MAXIMIZED WINDOW','\n')
        except:
            print('...','\n')
    def minimize_win(self,title='Untitled'):
        try:
            notepadWindow = gw.getWindowsWithTitle(title)[0]
            notepadWindow.minimize()
            if notepadWindow.isMinimize:
                print(title+' <-> MAXIMIZED WINDOW','\n')
        except:
            print('...','\n')
    def restore_win(self,title='Untitled'):
        try:
            gw.getWindowsWithTitle(title)[0].restore()
            if notepadWindo.resotre():
                print(title+' <-> RESTORE WINDOW','\n')
        except:
            print('...','\n')
    def resize_win(self,*lst):
        print(lst[0],lst[1],lst[2])
        try:
            gw.getWindowsWithTitle(lst[0])[0].resizeTo(lst[1],lst[2])
        except:
            print('...','\n')
    def move_win(self,*lst):
        try:
            gw.getWindowsWithTitle(lst[0])[0].moveTo(lst[1], lst[2])
        except:
            print('...','\n')
    def size_win(self,*lst):
        try:
            print(gw.getWindowsWithTitle(lst[0])[0].size,'\n')
        except:
            print('...','\n')
    def topleft_win(self,*lst):
        try:
            print('FROM ',gw.getWindowsWithTitle(lst[0])[0].topleft,'\n')
        except:
            print('...','\n')
    def bottomright_win(self,*lst):
        try:
            print('TO ',gw.getWindowsWithTitle(lst[0])[0].bottomright,'\n')
        except:
            print('...','\n')
    def width_win(self,*lst):
        try:
            print('WIDTH - ',gw.getWindowsWithTitle(lst[0])[0].width,'\n')
        except:
            print('...','\n')
    def height_win(self,*lst):
        try:
            print('HEIGHT - ',gw.getWindowsWithTitle(lst[0])[0].height,'\n')
        except:
            print('...','\n')
    def top_win(self,*lst):
        try:
            print('TOP - ',gw.getWindowsWithTitle(lst[0])[0].top,'\n')
        except:
            print('...','\n')
    def left_win(self,*lst):
        try:
            print('LEFT - ',gw.getWindowsWithTitle(lst[0])[0].left,'\n')
        except:
            print('...','\n')
    def close(self,*lst):
        try:
            nt=gw.getWindowsWithTitle(lst[0])[0]
            nt.close()
        except:
            print('...','\n')
app=WinInfo()
