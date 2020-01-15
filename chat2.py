
def read_file(filename):
	lines = []
	with open(filename,'r',encoding='utf-8-sig') as f: 
		for line in f:
			lines.append(line.strip())
	return lines
def convert(lines):
	person = None
	allen_word = 0
	viki_word = 0
	allen_sticks = 0
	viki_sticks = 0
	allen_image = 0
	viki_image = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticks +=1
			elif s[2] == '圖片':
				allen_image +=1
			else:
				for m in s[2:]:
					allen_word += len(m)
		if name == 'Viki':
			if s[2] == '貼圖':
				viki_sticks +=1
			elif s[2] == '圖片':
				viki_image +=1
			else:
				for m in s[2:]:
					viki_word += len(m)
	print('allen說了',allen_word,'個字','傳了',allen_sticks,'個貼圖',allen_image,'個圖片')
	print('viki說了',viki_word,'個字','傳了',viki_sticks,'個貼圖',viki_image,'個圖片')
	
def write_file(filename,lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines) #覆蓋
	#write_file('new_put.txt',lines)
main()