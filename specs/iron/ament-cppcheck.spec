# Meta Package
Name:           ros-iron-ament-cppcheck
Version:        0.14.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ament_cppcheck and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ament_cppcheck
Requires:       ros2-iron-ament_cppcheck-devel

Obsoletes: ros-iron-ament-cppcheck < 0.14.3-1

%description
The ability to perform static code analysis on C/C++ code using
Cppcheck and generate xUnit test result files.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.14.3-1
- Update to latest release
