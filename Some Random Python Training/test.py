import tkinter as tk
import time

class Speedometer:
    def __init__(self, root):
        self.speed = 0
        self.target_speed = 0
        self.root = root
        self.root.title("Speedometer")
        
        self.label = tk.Label(root, text="Speed: 0 km/h", font=("Helvetica", 24))
        self.label.pack(pady=20)
        
        self.accelerate_button = tk.Button(root, text="Accelerate", command=self.accelerate, width=15, height=2)
        self.accelerate_button.pack(side=tk.LEFT, padx=20, pady=20)
        
        self.decelerate_button = tk.Button(root, text="Decelerate", command=self.decelerate, width=15, height=2)
        self.decelerate_button.pack(side=tk.RIGHT, padx=20, pady=20)
        
        self.update_speed()

    def accelerate(self):
        self.target_speed += 10
        if self.target_speed > 200:
            self.target_speed = 200
    
    def decelerate(self):
        self.target_speed -= 10
        if self.target_speed < 0:
            self.target_speed = 0
    
    def update_speed(self):
        if self.speed < self.target_speed:
            self.speed += 1
        elif self.speed > self.target_speed:
            self.speed -= 1
        self.label.config(text=f"Speed: {self.speed} km/h")
        self.root.after(50, self.update_speed)

if __name__ == "__main__":
    root = tk.Tk()
    app = Speedometer(root)
    root.mainloop()
