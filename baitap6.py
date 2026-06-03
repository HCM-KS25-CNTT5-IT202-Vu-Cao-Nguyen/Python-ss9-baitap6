branch_names = [
    "Highlands Nhà Thờ",
    "Highlands Bà Triệu",
    "Highlands Nguyễn Du",
    "Highlands Landmark 81",
    "Highlands Trần Hưng Đạo"
]

daily_revenues = [
    15500000,
    28000000,
    9200000,
    45000000,
    11000000
]

target_achieved = [
    True,
    True,
    False,
    True,
    False
]

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====")
    print("1. Hiển thị báo cáo doanh thu tổng hợp")
    print("2. Thống kê chi nhánh Cao nhất / Thấp nhất")
    print("3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)")
    print("4. Thoát chương trình")
    print("================================================")

    try:
        choice = int(input("Nhập lựa chọn của bạn (1-4): "))

        if choice == 1:

            print("\n--- BÁO CÁO DOANH THU TỔNG HỢP ---")
            print(f"{'Tên Cơ Sở':<30} | {'Doanh Thu':<12} | {'Trạng Thái'}")
            print("-" * 65)

            for i in range(len(branch_names)):

                status = "Đạt" if target_achieved[i] else "Không Đạt"

                print(
                    f"{branch_names[i]:<30} | "
                    f"{daily_revenues[i]:<12} | "
                    f"{status}"
                )

            total_revenue = sum(daily_revenues)

            print("-" * 65)
            print(f"=> TỔNG DOANH THU TOÀN VÙNG: {total_revenue} VNĐ")

        elif choice == 2:

            highest_revenue = max(daily_revenues)
            lowest_revenue = min(daily_revenues)

            highest_index = daily_revenues.index(highest_revenue)
            lowest_index = daily_revenues.index(lowest_revenue)

            print("\nChi nhánh doanh thu cao nhất:")
            print(
                f"{branch_names[highest_index]} - "
                f"{highest_revenue} VNĐ"
            )

            print("\nChi nhánh doanh thu thấp nhất:")
            print(
                f"{branch_names[lowest_index]} - "
                f"{lowest_revenue} VNĐ"
            )

        elif choice == 3:

            failed_branches = []

            for i in range(len(branch_names)):

                if target_achieved[i] is False:
                    failed_branches.append(branch_names[i])

            print("\nDanh sách cơ sở không đạt chỉ tiêu:")
            print(failed_branches)

        elif choice == 4:

            print("Hệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!")
            break

        else:
            print(
                "[Lỗi] Lựa chọn không hợp lệ, "
                "vui lòng nhập lại số từ 1 đến 4!"
            )

    except ValueError:
        print(
            "[Lỗi] Lựa chọn không hợp lệ, "
            "vui lòng nhập lại số từ 1 đến 4!"
        )