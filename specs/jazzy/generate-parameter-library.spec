# Meta Package
Name:           ros-jazzy-generate-parameter-library
Version:        0.4.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-generate_parameter_library and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-generate_parameter_library
Requires:       ros2-jazzy-generate_parameter_library-devel

Obsoletes: ros-jazzy-generate-parameter-library < 0.4.0-1

%description
CMake to generate ROS parameter library.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.4.0-1
- Update to latest release
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.3.9-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.3.8-1
- Update to latest release
