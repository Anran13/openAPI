import tools

def main():
    data = tools.get_aqi(excel_name='aqi.xlsx')
    sitenames = tools.get_sitename(excel_name='aqi.xlsx')
    print(sitenames)

if __name__ == '__main__':
    main()


