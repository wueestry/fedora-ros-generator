# Meta Package
Name:           ros-humble-ament-clang-format
Version:        0.12.11
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ament_clang_format and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ament_clang_format
Requires:       ros2-humble-ament_clang_format-devel

Obsoletes: ros-humble-ament-clang-format < 0.12.11-1

%description
The ability to check code against style conventions using clang-format
and generate xUnit test result files.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.11-1
- Update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.10-1
- Update to latest release
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.9-1
- update to latest upstream
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.8-1
- update to latest release
* Fri Aug 11 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.7-1
- update to latest upstream
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.12.5-1
- Initial humble build
