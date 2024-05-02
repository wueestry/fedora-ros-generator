# Meta Package
Name:           ros-humble-launch-testing-ament-cmake
Version:        1.0.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-launch_testing_ament_cmake and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-launch_testing_ament_cmake
Requires:       ros2-humble-launch_testing_ament_cmake-devel

Obsoletes: ros-humble-launch-testing-ament-cmake < 1.0.5-1

%description
A package providing cmake functions for running launch tests from the
build.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.5-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.4-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.4-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.4-1
- Initial humble build
