class PromptMemory:
 def __init__(self):self.versions=[]
 def add(self,artifact):self.versions.append(artifact)
 def snapshot(self):return list(self.versions)
