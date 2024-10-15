# Meta Package
Name:           ros-jazzy-gz-dartsim-vendor
Version:        0.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://dartsim.github.io/
Summary:        Meta package for ros2-jazzy-gz_dartsim_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gz_dartsim_vendor
Requires:       ros2-jazzy-gz_dartsim_vendor-devel

Obsoletes: ros-jazzy-gz-dartsim-vendor < 0.0.2-1

%description
Vendor package for the DART physics engine v6.13.2

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.2-1
- Update to latest release
