# Meta Package
Name:           ros-iron-tlsf-cpp
Version:        0.15.0
Release:        1%{?dist}
License:        GNU Lesser Public License 2.1
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-tlsf_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-tlsf_cpp
Requires:       ros2-iron-tlsf_cpp-devel

Obsoletes: ros-iron-tlsf-cpp < 0.15.0-1

%description
C++ stdlib-compatible wrapper around tlsf allocator and ROS2 examples

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.15.0-1
- Update to latest release
