# Meta Package
Name:           ros-iron-generate-parameter-library
Version:        0.3.8
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-generate_parameter_library and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-generate_parameter_library
Requires:       ros2-iron-generate_parameter_library-devel

Obsoletes: ros-iron-generate-parameter-library < 0.3.8-1

%description
CMake to generate ROS parameter library.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.3.8-1
- Update to latest release
