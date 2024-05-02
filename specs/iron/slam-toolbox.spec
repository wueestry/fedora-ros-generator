# Meta Package
Name:           ros-iron-slam-toolbox
Version:        2.7.4
Release:        1%{?dist}
License:        LGPL
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-slam_toolbox and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-slam_toolbox
Requires:       ros2-iron-slam_toolbox-devel

Obsoletes: ros-iron-slam-toolbox < 2.7.4-1

%description
This package provides a sped up improved slam karto with updated SDK
and visualization and modification toolsets

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.7.4-1
- Update to latest release
