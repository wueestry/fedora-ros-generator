# Meta Package
Name:           ros-humble-tlsf-cpp
Version:        0.13.0
Release:        1%{?dist}
License:        GNU Lesser Public License 2.1
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-tlsf_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-tlsf_cpp
Requires:       ros2-humble-tlsf_cpp-devel

Obsoletes: ros-humble-tlsf-cpp < 0.13.0-1

%description
C++ stdlib-compatible wrapper around tlsf allocator and ROS2 examples

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.13.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.13.0-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.13.0-1
- Initial humble build
