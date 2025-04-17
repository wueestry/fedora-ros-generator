# Meta Package
Name:           ros-jazzy-popf
Version:        0.0.17
Release:        1%{?dist}
License:        GPLv2
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-popf and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-popf
Requires:       ros2-jazzy-popf-devel

Obsoletes: ros-jazzy-popf < 0.0.17-1

%description
The POPF package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.17-1
- Update to latest release
