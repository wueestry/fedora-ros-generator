# Meta Package
Name:           ros-iron-behaviortree-cpp-v3
Version:        3.8.6
Release:        1%{?dist}
License:        MIT
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-behaviortree_cpp_v3 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-behaviortree_cpp_v3
Requires:       ros2-iron-behaviortree_cpp_v3-devel

Obsoletes: ros-iron-behaviortree-cpp-v3 < 3.8.6-1

%description
This package provides the Behavior Trees core library.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.8.6-1
- Update to latest release
