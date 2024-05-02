# Meta Package
Name:           ros-iron-popf
Version:        0.0.15
Release:        1%{?dist}
License:        GPLv2
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-popf and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-popf
Requires:       ros2-iron-popf-devel

Obsoletes: ros-iron-popf < 0.0.15-1

%description
The POPF package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.0.15-1
- Update to latest release
