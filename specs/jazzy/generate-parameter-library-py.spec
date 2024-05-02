# Meta Package
Name:           ros-jazzy-generate-parameter-library-py
Version:        0.3.8
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-generate_parameter_library_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-generate_parameter_library_py
Requires:       ros2-jazzy-generate_parameter_library_py-devel

Obsoletes: ros-jazzy-generate-parameter-library-py < 0.3.8-1

%description
Python to generate ROS parameter library.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.3.8-1
- Update to latest release
