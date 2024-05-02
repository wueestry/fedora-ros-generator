# Meta Package
Name:           ros-iron-nav2-common
Version:        1.2.7
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-nav2_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-nav2_common
Requires:       ros2-iron-nav2_common-devel

Obsoletes: ros-iron-nav2-common < 1.2.7-1

%description
Common support functionality used throughout the navigation 2 stack

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.7-1
- Update to latest release
